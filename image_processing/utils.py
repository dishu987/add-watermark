from imutils import paths
import numpy as np
import argparse
import cv2
import os


def get_watermark_image(watermark_url,image_url,output_url,flag,alpha):
        imageDir = image_url #path of the folder where the input images are stored 
        outputDir=output_url#path of the folder where the ouput images will be stored
        waterMarks = watermark_url #path of the watermark
        watermark = cv2.imread(waterMarks)
        (wH, wW,ch1) = watermark.shape
        wH_static = wH
        wW_static = wW
        if(ch1==None):
            watermark=cv2.cvtColor(watermark,cv2.COLOR_BGR2RGB)
            (wH, wW,ch1) = watermark.shape
        if(ch1<4):
            watermark=cv2.cvtColor(watermark,cv2.COLOR_BGR2RGB)
            watermark  = np.dstack([watermark, np.ones((wH, wW), dtype="uint8") * 255])
            (wH, wW,ch1) = watermark.shape 
        if(ch1>4):
               watermark=cv2.cvtColor(watermark,cv2.COLOR_BGR2RGB)
               watermark  = np.dstack([watermark, np.ones((wH, wW), dtype="uint8") * 255])
               (wH, wW,ch1) = watermark.shape 
        (B, G, R, A) = cv2.split(watermark)
        B = cv2.bitwise_and(B, B, mask=A)
        G = cv2.bitwise_and(G, G, mask=A)
        R = cv2.bitwise_and(R, R, mask=A)
        watermark = cv2.merge([B, G, R, A])
        print(wW)
        print(wH)
        print(watermark.shape)
        for root,dirs,files in os.walk(imageDir):
            for file in files:
                fullfilepath=root+'/'+file
                image = cv2.imread(fullfilepath,cv2.IMREAD_UNCHANGED)
                (h, w,ch) = image.shape
                watermark = cv2.imread(waterMarks,cv2.IMREAD_UNCHANGED)
                (wH,wW,ch1)= watermark.shape
                if flag==1:
                    watermark=cv2.resize(watermark,(int(0.095*w),int(0.105*h)))
                else: 
                       watermark=cv2.resize(watermark,(int(0.28*w),int(0.08*h)))
                wH,wW,ch1= watermark.shape
                if(ch1==None):
                   watermark=cv2.cvtColor(watermark,cv2.COLOR_BGR2RGB)
                   (wH, wW,ch1) = watermark.shape
                if(ch1<4):
                    watermark=cv2.cvtColor(watermark,cv2.COLOR_BGR2RGB)
                    watermark  = np.dstack([watermark, np.ones((wH, wW), dtype="uint8") * 255])
                    (wH, wW,ch1) = watermark.shape 
                if(ch1>4):
                    watermark=cv2.cvtColor(watermark,cv2.COLOR_BGR2RGB)
                    watermark  = np.dstack([watermark, np.ones((wH, wW), dtype="uint8") * 255])
                    (wH, wW,ch1) = watermark.shape 
                #if(wH+10>=h or wW+10>=w):
                 #   watermark=cv2.resize(watermark,(150,100))
                  #  (wH,wW) = watermark.shape[:2]
                   # image=cv2.resize(image,(1280,720))
                    #(h, w) = image.shape[:2]
                (B, G, R, A) = cv2.split(watermark)
                B = cv2.bitwise_and(B, B, mask=A)
                G = cv2.bitwise_and(G, G, mask=A)
                R = cv2.bitwise_and(R, R, mask=A)
                watermark = cv2.merge([B, G, R, A])
                if(ch<4):
                   while(ch!=4):
                     image  = np.dstack([image, np.ones((h, w), dtype="uint8") * 255])
                     (h, w,ch) = image.shape 
                if ch>4:
                    image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
                    image  = np.dstack([image, np.ones((h, w), dtype="uint8") * 255])
                (h,w,ch) = image.shape
                overlay = np.zeros((h, w, 4), dtype="uint8")
                #shapes = np.zeros_like(image,np.uint8)
                #shapes[h-10-wH:h-10,w-10-wW:w-10] = watermark
                #mask=shapes.astype(bool) 
                #image[mask] = cv2.addWeighted(image,1-alpha,shapes,alpha,None)[mask]
                output = image.copy()
                print(output.shape)
                print(watermark.shape)
                #print(wH)
                #print(wW)
                #print(h)
                #print(w)
                overlay[h -wH-10:h-10,w-10-wW:w-10] = watermark
                res = cv2.addWeighted(overlay, alpha, output, 1.0,None)
                filename = outputDir+'/new'+file
                cv2.imwrite(filename, res)
                return 'new'+file
        cv2.destroyAllWindows()
