#-----------------------------------------------
#librerias
#------------------------------------------------
import mediapipe as mp
import cv2
# declaracion de variables
hands = mp.solutions.hands
deteccion = hands.Hands()
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0) 
# bucle para detectar las manos y los dedos
while True:
    ok, frame = cap.read()
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    resultado = deteccion.process(rgb)
    if resultado.multi_hand_landmarks:
        for mano in resultado.multi_hand_landmarks:
            
  
            listaddos = [] #Lista para almacenar el estado de los dedos
            mp_drawing.draw_landmarks(frame, mano, hands.HAND_CONNECTIONS)
            #deo indice
            punto6 = mano.landmark[6].y
            punto8 = mano.landmark[8].y
            if punto8 < punto6:
                listaddos.append(1)
                print("dedo índice levantado")
            else:
                listaddos.append(0)
                print("dedo índice abajo")
            #dedo medio
            punto10 = mano.landmark[10].y
            punto12 = mano.landmark[12].y
            if punto12 < punto10:
                listaddos.append(1)
                print("dedo de enmedio levantado") 
            else:
                listaddos.append(0)
                print("dedo de enmedio abajo")
            #dedo anular
            punto14 = mano.landmark[14].y
            punto16 = mano.landmark[16].y
            if punto16 < punto14:
                listaddos.append(1)
                print("dedo anular levantado") 
            else:
                listaddos.append(0)
                print("dedo anular abajo")
            #dedo meñique
            punto18 = mano.landmark[18].y   
            punto20 = mano.landmark[20].y
            if punto20 < punto18:
                listaddos.append(1)
                print("dedo meñique levantado") 
            else:
                listaddos.append(0)
                print("dedo meñique abajo")
            #deedo pulgar
            punto2 = mano.landmark[2].x
            punto4 = mano.landmark[4].x
            
            
            muneca = mano.landmark[0].x
            menique = mano.landmark[17].x
            
            if muneca > menique:
                 print("mano derecha")
            else:
                print("mano izquierda")
            if muneca > menique and punto4 > punto2:
                listaddos.append(1)
                print("pulgar derecho levantado")
            elif muneca > menique and punto4 < punto2:
                listaddos.append(0)
                print("pulgar derecho abajo")
            elif muneca < menique and punto4 < punto2:
                listaddos.append(1)
                print("pulgar izquierdo levantado")
            elif muneca < menique and punto4 > punto2:
                listaddos.append(0)
                print("pulgar izquierdo abajo")

        mensaje = "".join(str(d) for d in listaddos)#Convierte la lista de estados de los dedos en una cadena de texto
        print("mensaje:", mensaje)#Imprime el mensaje que representa el estado de los dedos (1 para levantado, 0 para abajo)
        print("pulgar:", punto4, punto2)#Imprime las coordenadas del pulgar para verificar su posición
            



  


    cv2.imshow("Frame", frame) #Muestra el video con las manos detectadas
    if cv2.waitKey(1) & 0xFF == ord('q'): #Si se presiona la tecla 'q', se sale del bucle
     break  #Libera la cámara y cierra las ventanas
    

    

    
