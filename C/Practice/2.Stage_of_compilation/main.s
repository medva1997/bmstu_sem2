	.file	"main.c"
	.intel_syntax noprefix
	.globl	work
	.data
	.align 4
	.type	work, @object
	.size	work, 4
work:
	.long	1
	.globl	myarray
	.align 16
	.type	myarray, @object
	.size	myarray, 16
myarray:
	.long	1
	.long	2
	.long	3
	.long	4
	.section	.rodata
.LC0:
	.string	"%d\n"
	.text
	.globl	print
	.type	print, @function
print:
.LFB0:
	.cfi_startproc
	push	rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	mov	rbp, rsp
	.cfi_def_cfa_register 6
	sub	rsp, 16
	mov	DWORD PTR [rbp-4], edi
	mov	eax, DWORD PTR [rbp-4]
	mov	esi, eax
	mov	edi, OFFSET FLAT:.LC0
	mov	eax, 0
	call	printf
	nop
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE0:
	.size	print, .-print
	.globl	main
	.type	main, @function
main:
.LFB1:
	.cfi_startproc
	push	rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	mov	rbp, rsp
	.cfi_def_cfa_register 6
	sub	rsp, 16
	mov	DWORD PTR [rbp-12], 1
	mov	DWORD PTR [rbp-8], 1
	mov	DWORD PTR [rbp-4], 0
	jmp	.L3
.L4:
	mov	eax, DWORD PTR [rbp-8]
	add	DWORD PTR [rbp-12], eax
	mov	eax, DWORD PTR [rbp-12]
	sub	eax, DWORD PTR [rbp-8]
	mov	DWORD PTR [rbp-8], eax
	mov	eax, DWORD PTR [rbp-12]
	mov	edi, eax
	call	print
	add	DWORD PTR [rbp-4], 1
.L3:
	cmp	DWORD PTR [rbp-4], 9
	jle	.L4
	mov	eax, 0
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE1:
	.size	main, .-main
	.ident	"GCC: (Ubuntu 5.3.1-14ubuntu2.1) 5.3.1 20160413"
	.section	.note.GNU-stack,"",@progbits
