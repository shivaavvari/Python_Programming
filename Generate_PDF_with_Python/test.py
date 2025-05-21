
from fpdf import FPDF, XPos,YPos
from pathlib import Path 

pth = Path('D://inligntech')

list_of_dirs =[dir.name for dir in  pth.iterdir()if dir.is_dir() and dir.name != '.git']
res = next(iter(list_of_dirs))

for i in range(1, 6):
    print(res)
