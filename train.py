import torch
from torch import nn
# from Unet_ import Unet
from Unet import Unet
from sample import MydataSet
from torch.utils.data import DataLoader
from torch import optim
import os
from evaluation import get_DC

if __name__ == '__main__':
    dataset = MydataSet()
    dataloader = DataLoader(dataset, batch_size=1, shuffle=True, num_workers=4)
    module = Unet(1, 1).cuda()
    # if os.path.exists('params/params0.pth'):
    #     module.load_state_dict(torch.load('params/params0.pth'))
    #     print('加载模型ing')
    optimizer = optim.Adam(module.parameters())
    criticizer = nn.BCELoss()
    for epoch in range(1000):
        for i, (data, lable) in enumerate(dataloader):
            data = data.cuda()
            lable = lable.cuda()
            output = module(data, )  # L=2
            loss1 = criticizer(output, lable)
            # loss2 = 1 - get_DC(output.cpu(),lable.cpu())
            # print(loss1.item(), loss2.item())
            # loss = loss1 + loss2
            # print(loss1.item(),loss2)
            optimizer.zero_grad()
            loss1.backward()
            optimizer.step()
            if i % 10 == 0:
                print('epoch: {} | loss: {} | len {}'.format(epoch, loss1.item(), i))
        torch.save(module.state_dict(), r'params\params{}.pth'.format(epoch))
