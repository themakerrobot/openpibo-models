# deploy
python3 setup.py bdist_wheel  
twine upload dist/*

# docs
sudo apt install python3-sphinx -y  
pip3 install myst-parser  
pip3 install sphinx_rtd_theme

# vim
<pre><code>
curl -O https://raw.githubusercontent.com/nanotech/jellybeans.vim/master/colors/jellybeans.vim
sudo cp jellybeans.vim /usr/share/vim/vim{버전}/colors/
sudo cp jellybeans.vim /home/pi/.vim/colors/

sudo vi /usr/share/vim/vimrc / ~/.vimrc

set mouse=c
set paste
syntax on
set autoindent
set cindent
set ts=2
set shiftwidth=2
set laststatus=2
set hlsearch
set smartcase
set smarttab
set smartindent
colorscheme jellybeans
</code></pre>
