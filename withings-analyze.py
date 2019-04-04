#! /usr/bin/env python3

import sys
from struct import unpack

def sr(f,offs,size):
	f.seek(offs)
	return f.read(size)

def i(f,offs,size):
	f.seek(offs)
	if size==2:
		return unpack('<H',f.read(2))[0]
	elif size==4:
		return unpack('<I',f.read(4))[0]
	else:
		raise 'Dead'

def dump_section_header(f, offset, fnameprefix):
	section_type = i(f,offset,2)
	section_len = i(f,offset+2,2)

	print('Entry type: %s (%s bytes)'% (section_type, section_len))

	if True:
		f.seek(offset+0x04)
		for a in range(section_len):
			byte = f.read(1)[0]
			print(" %0.2X"%byte, end='')
		print('')

	if section_type in [1,4,7,8]:
		if section_type == 1:
			print(" Type: main firmware")
		if section_type == 4:
			print(" Type: boot loader")
		if section_type == 7:
			print(" Type: unknown")
		if section_type == 8:
			print(" Type: unknown")
		print(' %s bytes @ %s (ends at %s)' % (i(f,offset + 0x08,4),i(f,offset + 0x04,4),i(f,offset + 0x08,4)+i(f,offset + 0x04,4)-1))
		print(' dd if=%s of=%s bs=1 count=%s skip=%s' % (fnameprefix, fnameprefix+'.'+str(section_type),i(f,offset + 0x08,4),i(f,offset + 0x04,4)))


		print(' CRC: 0x%0.4X' % i(f,offset + 0x0c,4))
		print(' Version: %s' % i(f,offset + 0x10,4))
		print('')

	return 4+section_len


def dump_file_header(f):
	print('= File header =')
	# print('Header version[=1]: %s'% i(f, 0, 2))
	# print('Header content length[=80]: %s'% i(f, 2, 2))
	if 1 != i(f,0,2):
		raise Exception("Incorrect file format (wrong header version)")
	if i(f,2,2) != 80:
		raise Exception("Incorrect file format (wrong content length)")
	print('Header checksum: %s'% i(f,4+2*40, 4))
	print('')
	return (4, i(f, 2, 2))

with open(sys.argv[1], 'rb') as f:
	(firstoffs,maxlen)=dump_file_header(f)
	offs = firstoffs
	while offs < firstoffs + maxlen:
		offs = offs + dump_section_header(f,offs, sys.argv[1])

