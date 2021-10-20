; Author: Md Salman Rahman
; Course: CYBI-6302-91L
; Instructor: Dr. Jose Poveda
; Problem: Write a computer program in assembly language for the processor family Intel x86-32 
; that reads two signed interger numbers from the keyboard and writes them in ascending order on the console.


section .data
  request db 'Enter two integer numbers: ',0
  message db "The ascending order is %d, %d", 10, 0
  integer1 times 4 db 0 ; 32-bits integer = 4 bytes
  integer2 times 4 db 0 ; 32-bits integer = 4 bytes
  formatin db "%d%d",0


section .text
  global main
  extern printf
  extern scanf

main:
  ; Ask for an integer with printf(request)
  push request
  call printf
  add esp, 4                               ; remove parameters from the stack


 ; Read user input with scanf("%d%d",integer1, integer2)
  push integer2
  push integer1
  push formatin
  call scanf
  add esp, 16



; Move the values under the addresses integer1 and integer2
  ; to EAX and EBX and add both values
  mov eax, [integer1]
  mov ebx, [integer2]

  ; Compare eax, ebx to get in eax the greatest integer number as we will make ascending using this
  cmp eax, ebx
  	jl _ref2
  	jmp _exit
  _ref2:
  	mov eax, ebx
  	mov ebx, [integer1]
  	jmp _exit
  
  
; Print out the greatest integer in ascending order
_exit:
      push eax
      push ebx
      push message
      call printf
      add esp, 8
      
  ; Linux terminate the app
  mov eax, 1
  mov ebx, 0 
  int 80h 
      
