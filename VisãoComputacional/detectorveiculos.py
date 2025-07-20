import torch
import torch.nn as nn
import torch.optim as optim
import torchvision.transforms as transforms
import torchvision.datasets as datasets
from torch.utils.data import DataLoader, random_split
import segmentation_models_pytorch as smp
import matplotlib.pyplot as plt
import numpy as np
from torchvision.transforms.functional import pil_to_tensor

# Verifica GPU
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"\U0001F680 Dispositivo usado: {DEVICE}")
if DEVICE == "cpu":
    print("⚠️ Aviso: O código está rodando na CPU. Isso pode ser muito lento!")

# Hiperparâmetros
BATCH_SIZE = 16
EPOCHS = 10
LR = 0.001

# Transformações de imagem
image_transform = transforms.Compose([
    transforms.Resize((256, 256)),
    transforms.ToTensor()
])

def process_mask(x):
    return torch.clamp(pil_to_tensor(x).squeeze().long(), 0, 20)

mask_transform = transforms.Compose([
    transforms.Resize((256, 256)),
    transforms.Lambda(process_mask)
])

# Definição da função de visualização
def visualize_sample(model, dataloader):
    model.eval()
    with torch.no_grad():
        images, masks = next(iter(dataloader))
        images, masks = images.to(DEVICE), masks.to(DEVICE)
        outputs = model(images)
        outputs = torch.argmax(outputs, dim=1).cpu().numpy()
        images = images.cpu().numpy()
        masks = masks.cpu().numpy()

        fig, axes = plt.subplots(3, min(4, BATCH_SIZE), figsize=(12, 6))
        for i in range(min(4, BATCH_SIZE)):
            axes[0, i].imshow(np.transpose(images[i], (1, 2, 0)))
            axes[0, i].axis("off")
            axes[1, i].imshow(masks[i], cmap="gray")
            axes[1, i].axis("off")
            axes[2, i].imshow(outputs[i], cmap="gray")
            axes[2, i].axis("off")
        plt.show()

if __name__ == '__main__':
    # Carregamento do dataset
    dataset = datasets.VOCSegmentation(root="./data", year="2012", image_set="train", download=True, 
                                       transform=image_transform, target_transform=mask_transform)
    train_size = int(0.8 * len(dataset))
    val_size = len(dataset) - train_size
    dataset_train, dataset_val = random_split(dataset, [train_size, val_size])

    # Definição dos DataLoaders
    dataloader_train = DataLoader(dataset_train, batch_size=BATCH_SIZE, shuffle=True, num_workers=0, pin_memory=True)
    dataloader_val = DataLoader(dataset_val, batch_size=BATCH_SIZE, shuffle=False, num_workers=0, pin_memory=True)


    # Modelo
    model = smp.Unet(encoder_name="resnet34", classes=21, activation=None).to(DEVICE)

    # Função de perda e otimizador
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.AdamW(model.parameters(), lr=LR)

    # Treinamento
    best_val_loss = float('inf')
    for epoch in range(EPOCHS):
        model.train()
        total_loss = 0
        
        for images, masks in dataloader_train:
            images, masks = images.to(DEVICE), masks.to(DEVICE)
            
            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, masks.long())
            loss.backward()
            optimizer.step()
            
            total_loss += loss.item()
        
        # Validação
        model.eval()
        val_loss = 0
        with torch.no_grad():
            for images, masks in dataloader_val:
                images, masks = images.to(DEVICE), masks.to(DEVICE)
                outputs = model(images)
                val_loss += criterion(outputs, masks.long()).item()
        
        val_loss /= len(dataloader_val)
        print(f"Epoch {epoch+1}/{EPOCHS}, Loss: {total_loss/len(dataloader_train):.4f}, Val Loss: {val_loss:.4f}")

        # Salvar o melhor modelo
        if val_loss < best_val_loss:
            best_val_loss = val_loss
            torch.save(model.state_dict(), "best_unet_model.pth")
            print("✅ Melhor modelo salvo!")

    # Exibir amostra de previsão
    visualize_sample(model, dataloader_val)
