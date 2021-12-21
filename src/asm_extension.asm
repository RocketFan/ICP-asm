global add42

add42:
    push rbp
    mov rbp, rsp
    mov rax, rdi
    add rax, 42
    mov rsp, rbp
    pop rbp
    ret