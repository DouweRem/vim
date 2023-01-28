function! MyHighlights() abort
    highlight Conceal     gui=NONE guibg=NONE guifg=#a4bd81
endfunction

augroup MyColors
    autocmd!
    autocmd ColorScheme * call MyHighlights()
augroup END

call plug#begin('~/.vim/plugged')

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

Plug 'ycm-core/youcompleteme'
let g:ycm_key_list_select_completion = ['<C-n>', '<Down>']
let g:ycm_key_list_previous_completion = ['<C-p>', '<Up>']

Plug 'ervandew/supertab'
let g:SuperTabDefaultCompletionType = '<C-n>'

Plug 'dracula/vim',{'as':'dracula'}

Plug 'sainnhe/everforest',{'as':'everforest'}
set background=dark

call plug#end()

colorscheme everforest
