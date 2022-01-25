section .data
    zero: dd 0
    point: dd 0, 0
    bool: dd 0
    ptr1: dq 0
    ptr2: dq 0

section .text
    global _find_closest_point

_find_closest_point:
    push rbp
    mov rbp, rsp

    mov [rel ptr1], rax
    mov [rel ptr2], rcx

    mov rcx, [rel ptr1]
    movlps xmm0, [rcx]

    mov rcx, 0
    mov rbx, [rel ptr2]

    movlps xmm1, [rbx]
    subps xmm1, xmm0
    mulps xmm1, xmm1
    movlps [rel point], xmm1

    movq xmm1, [rel point]
    movq xmm2, [rel point + 4]
    addss xmm1, xmm2

    movss xmm3, xmm1
    mov rax, rbx

    loop1:
        movlps xmm1, [rbx]
        subps xmm1, xmm0
        mulps xmm1, xmm1
        movlps [rel point], xmm1

        movq xmm1, [rel point]
        movq xmm2, [rel point + 4]
        addss xmm1, xmm2

        movss xmm2, xmm1
        cmpltss xmm1, xmm3
        movq [rel bool], xmm1
        cmp [rel bool], dword 0
        je next1

        movss xmm3, xmm2
        mov rax, rbx
        
        next1:
            add rbx, 8
            add rcx, 2
            cmp rcx, rdx
            jne loop1

    mov rsp, rbp
    pop rbp
    ret