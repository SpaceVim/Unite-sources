function! unicode#groups()

    return map(split(globpath(g:unite_unicode_data_path, '*.txt'), '\n'),
          \ '[fnamemodify(v:val, ":t:r"), fnamemodify(v:val, ":p")]')

endfunction

function! unicode#words(groups)

    let unicode = []
    call map(a:groups, 'extend(unicode, readfile(g:unite_unicode_data_path . v:val . ".txt"))')
    return unicode

endfunction
