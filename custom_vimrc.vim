call plug#begin('C:\Program Files (x86)\Vim\vim82\plugged')

Plug 'lervag/vimtex'
let g:tex_flavor='latexmk'
let g:vimtex_view_method='general'
let g:vimtex_quickfix_mode=0
set conceallevel=2
hi clear Conceal
let g:tex_conceal='abdmg'

Plug 'SirVer/ultisnips'
let g:UltiSnipsExpandTrigger = '<tab>'
let g:UltiSnipsJumpForwardTrigger = '<tab>'
let g:UltiSnipsJumpBackwardTrigger = '<s-tab>'


Plug 'dracula/vim',{'as':'dracula'}

call plug#end()

colorscheme dracula
