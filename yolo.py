import torch

model= torch.hub.load('ultralytics/yolov5', 'yolov5s',pretrained=True)
img='https://th.bing.com/th/id/OIP.r9wE067b2FCyRlzs1ZwtfAHaE8?w=299&h=200&c=7&r=0&o=5&dpr=1.3&pid=1.7'
results= model(img)
results.show()
print(results.pandas().xyxy[0])
