"""
Global settings for use

Created by Kunhong Yu
Date: 2020/05/19
"""
class Config():
    """
    All parameters:
        --use_gpu: True or False
        --verification: default is True,
        --extend_format: default is 'jpg',
        --folder: default is os.path.join('./data', 'test')
    """

    #Map from capital number to real index or the other way around#
    vocab = dict(zip(range(26), [chr(i) for i in range(65, 65 + 26)]))
    inversed_vocab = dict(zip([chr(i) for i in range(65, 65 + 26)], range(26)))

    model_str = 'lenet'

    use_gpu = True
    verification = True
    extend_format = 'jpg'
    # def __init__(self, picPath):
    #     print(picPath)#####传入指定pic路径
    folder = './data'

    def parse(self, kwargs):
        """This function is used to modify configurations according to user's input"""
        if len(kwargs) == 0:
            print('The input is empty, use set hyper parameters')
        else:
            for k, v in kwargs.items():
                if not hasattr(self, k):
                    print('This parameter does not exist, will be added.')
                setattr(self, k, v)