from PIL import Image
from mmocr.utils.ocr import MMOCR


# Classes
class OCR:
    def __init__(self, detection_model_name='DB_r18', recognizer_model_name='RobustScanner', device='cpu', merge=True,
                 details=True):
        self.ocr_model = MMOCR(config_dir="~/mmocr/configs/",
                               det=detection_model_name,
                               recog=recognizer_model_name,
                               # kie='SDMGR',
                               device=device)
        self.merge = merge
        self.details = details

    def get_text(self, image_path, output_file='temp_ocr.jpg'):
        results = self.ocr_model.readtext(image_path, output=output_file, merge=self.merge, details=self.details)
        img = Image.open(output_file)
        return [img, results[0]["result"]]


ocr_model = OCR()
