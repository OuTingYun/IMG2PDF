import os
import PIL
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import landscape


def genpdf(pdfname,pagesizes):
    pdf = canvas.Canvas(os.path.dirname(os.path.abspath(__file__))+'\\PDF\\'+pdfname)
    pdf.setPageSize(pagesizes)
    return pdf

def save_img_to_pdf(pdf,image,x,y,w,h):
    pdf.drawImage(image,x,y,w,h)
    pdf.showPage()
def get_max_img_size(Imgs):
    Imgs_w=[]
    Imgs_h=[]
    for img in Imgs:
        w,h=img.size
        Imgs_w.append(w)
        Imgs_h.append(h)
    Max_w=max(Imgs_w)
    Max_h=max(Imgs_h)
    return (Max_w,Max_h)

if __name__ == '__main__':    
    
    
    #輸入pdf名稱
    print("Input PDF's Name")
    pdf_name=input()

    #讀取Picture
    folder =os.path.dirname(os.path.abspath(__file__))+ '\Img'
    des=os.path.dirname(os.path.abspath(__file__))+'\PDF'
    filelist = os.listdir(folder)
    # print(folder)
    Imgs_path=[folder+'\\'+filename for filename in filelist]
    Imgs=[PIL.Image.open(path) for path in Imgs_path]
    # print(Imgs)
    #取得圖片大小
    pdf_size = get_max_img_size(Imgs)
    #製造PDF大小
    my_pdf = genpdf(f'{pdf_name}.pdf',pdf_size)

    for img,path in zip(Imgs,Imgs_path):
        img_x = 0
        img_y = 0
        save_img_to_pdf(my_pdf,path,x=img_x,y=img_y,w=pdf_size[0],h=pdf_size[1])
    my_pdf.save()
    print(f"\nSave in {des}\{pdf_name}.pdf \n")