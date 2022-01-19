section .data
    abc: dd 100

section .text
    global add42

add42:
    push rbp
    mov rbp, rsp
    movq xmm0, rcx
    mov rax, rcx
    add rax, 42
    mov rsp, rbp
    pop rbp
    ret