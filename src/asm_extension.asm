section .data
    point: dd 0, 0
    bool: dd 0
    ptr1: dq 0
    ptr2: dq 0


section .text
    global _find_closest_point


# Finds closest point in array to passed reference point
_find_closest_point:
    # Save stack position
    push rbp
    mov rbp, rsp

    mov [rel ptr1], rax # reference point pointer to variable
    mov [rel ptr2], rcx # array of points pointer to variable

    # move point to xmm0
    mov rcx, [rel ptr1]
    movlps xmm0, [rcx]

    mov rcx, 0 # set loop counter to 0
    mov rbx, [rel ptr2] # move array of points pointer to rbx

    # Calculate vector beetwen reference point and point in array
    movlps xmm1, [rbx] # move first point from array to xmm1
    subps xmm1, xmm0 # difference vector from two points
    mulps xmm1, xmm1 # vector to second power
    movlps [rel point], xmm1 # move vector to variable

    # Sum up vector elements to get the squared distance
    movq xmm1, [rel point]
    movq xmm2, [rel point + 4]
    addss xmm1, xmm2

    # Save closest point data
    movss xmm3, xmm1 # Save squared distance
    mov rax, rbx  # Save point pointer

    # Loop over all points in array
    loop1:
        # Calculate vector beetwen reference point and point in array
        movlps xmm1, [rbx] # move point from array to xmm1
        subps xmm1, xmm0 # difference vector from two points
        mulps xmm1, xmm1 # vector to second power
        movlps [rel point], xmm1 # move vector to variable

        # Sum up vector elements to get the squared distance
        movq xmm1, [rel point]
        movq xmm2, [rel point + 4]
        addss xmm1, xmm2

        # Check if the current point is closer than saved point
        movss xmm2, xmm1
        cmpltss xmm1, xmm3
        movq [rel bool], xmm1
        cmp dword [rel bool], dword 0
        je next1 # If current point is further jump to next1

        # Save closest point data
        movss xmm3, xmm2 # Save squared distance
        mov rax, rbx # Save point pointer
        
        # Control loop flow
        next1:
            add rbx, 8 # Increment array pointer to next point
            add rcx, 2 # Increment loop counter
            cmp rcx, rdx # Check if it's the end of an array
            jne loop1 # Ends loop 

    # Return from function
    mov rsp, rbp
    pop rbp
    ret