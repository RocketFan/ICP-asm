section .data
    abc: dd 100

section .text
    global _find_closest_point

_find_closest_point:
    push rbp
    mov rbp, rsp

    ; movq xmm0, [rdi]

    mov rsp, rbp
    pop rbp
    ret

add42:
    push rbp
    mov rbp, rsp
    movq xmm0, rdi
    mov rax, rdi
    add rax, 42
    mov rsp, rbp
    pop rbp
    ret