import cv2
import numpy as np

# Carregar o classificador de carros
car_cascade = cv2.CascadeClassifier("C:/Users/pedro/OneDrive/Documentos/Trabalhos e codigos UTFPR/VISAO COMPUTACIONAL/TRAB5/cars.xml")

def non_max_suppression(boxes, overlap_thresh=0.3):
    if len(boxes) == 0:
        return []

    boxes = sorted(boxes, key=lambda x: x[1], reverse=False)
    pick = []

    while len(boxes) > 0:
        box = boxes.pop(0)
        remaining_boxes = []
        for b in boxes:
            x1, y1, w1, h1 = box
            x2, y2, w2, h2 = b
            
            xx1 = max(x1, x2)
            yy1 = max(y1, y2)
            xx2 = min(x1 + w1, x2 + w2)
            yy2 = min(y1 + h1, y2 + h2)
            
            inter_width = max(0, xx2 - xx1)
            inter_height = max(0, yy2 - yy1)
            inter_area = inter_width * inter_height
            
            area1 = w1 * h1
            area2 = w2 * h2
            union_area = area1 + area2 - inter_area
            
            overlap = inter_area / union_area
            
            if overlap < overlap_thresh:
                remaining_boxes.append(b)

        pick.append(box)
        boxes = remaining_boxes

    return pick

def detect_vehicles(image_path, output_path="detected_vehicles.jpg"):
    img = cv2.imread(image_path)
    
    if img is None:
        print("Erro ao carregar a imagem. Verifique o caminho.")
        return
    
    # Converter para escala de cinza
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Aplicar equalização de histograma para melhorar contraste
    gray = cv2.equalizeHist(gray)

    # Aplicar desfoque gaussiano para reduzir ruídos
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    
    vehicles = []
    for scaleFactor in [1.02, 1.05]:  # Detectar objetos menores
        for minNeighbors in [2, 3]:  # Reduzir perda de veículos detectados
            detected = car_cascade.detectMultiScale(
                gray, scaleFactor=scaleFactor, minNeighbors=minNeighbors, minSize=(30, 30)
            )
            vehicles.extend(detected)
    
    unique_vehicles = non_max_suppression(vehicles, overlap_thresh=0.3)
    
    if len(unique_vehicles) == 0:
        print("Nenhum veículo detectado.")
    else:
        print(f"{len(unique_vehicles)} veículo(s) detectado(s).")
    
    # Desenhar retângulos nos veículos detectados
    for (x, y, w, h) in unique_vehicles:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    # Exibir e salvar a imagem processada
    cv2.imshow("Detecção de Veículos", img)
    cv2.imwrite(output_path, img)
    print(f"Imagem salva em {output_path}")
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Teste com a imagem (verifique o caminho)
detect_vehicles("C:/Users/pedro/OneDrive/Documentos/Trabalhos e codigos UTFPR/VISAO COMPUTACIONAL/TRAB5/imagem1.jpg", 
                output_path="C:/Users/pedro/OneDrive/Documentos/Trabalhos e codigos UTFPR/VISAO COMPUTACIONAL/TRAB5/imagem_com_deteccao.jpg")
