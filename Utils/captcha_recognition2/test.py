"""
Testing file for using

Created by Kunhong Yu
Date: 2020/05/19
"""
import torch as t
from config import Config
import os
import fire
from public.captcha_recognition2.utils import get_dataloader, get_preds
from public.captcha_recognition2.models import LeNet
from public.captcha_recognition2.config import Config

def test_model(**kwargs):
    """This function is used to test model"""
    opt = Config()
    opt.parse(kwargs)

    if opt.use_gpu:
        t.set_default_tensor_type('torch.cuda.FloatTensor')
    else:
        t.set_default_tensor_type('torch.FloatTensor')

    device = t.device('cuda') if opt.use_gpu else t.device('cpu')

    #load the model#
    model = LeNet()
    #model.load_state_dict(t.load('./checkpoints' + os.sep + opt.model_str + os.sep + 'saved_model.pth', map_location = device))
    model.load_state_dict(t.load('./public/captcha_recognition2/checkpoints' + os.sep + opt.model_str + os.sep + 'saved_model.pth', map_location = device))
    #path = os.path.abspath('.') + r"\checkpoints\lenet\saved_model.pth"
    #model.load_state_dict(t.load(path, map_location = device))
    model.to(device)
    model.eval()

    dataloader = get_dataloader(inverse_vocab = opt.inversed_vocab,
                                verification = opt.verification,
                                extend_format = opt.extend_format,
                                folder = opt.folder)

    string = ''
    for i, (batch_x, batch_y) in enumerate(dataloader):
        batch_x = batch_x.to(device)
        if opt.verification:
            batch_y = batch_y.long().to(device)
        outputs = model(batch_x)
        preds = get_preds(outputs)

        for j in range(batch_x.size(0)):
            pred = preds[j].cpu().numpy().tolist()
            pred = ([opt.vocab[kk] for kk in pred])
            pred = ''.join(pred)
            string += pred
            #print(string)
    return string


# def main(**kwargs):
#     codeStr = test_model(**kwargs)
#     print(codeStr)
#     return codeStr

if __name__ == '__main__':
    #fire.Fire()
    pass

"""
Usage:
python3 test.py main \
    --use_gpu=True\
    --verification=True\
    --extend_format='jpg'\
    --folder='./data'
"""