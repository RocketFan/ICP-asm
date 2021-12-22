section .data
    abc: dd 100

section .text
    global add42

add42:
    push rbp
    mov rbp, rsp
    push rdi
    movq xmm0, rdi
    mov rax, rdi
    add rax, 42
    mov rsp, rbp
    pop rbp
    ret