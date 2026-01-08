def calculate_share_rate(value, tax, calc):
	ngr = (value - (value*0.12)) * tax
	ggr = value * tax

	if calc == 'ggr':
		return ggr
	else:
		return ngr

if __name__ == "__main__":
    value = float(input('value: '))
    tax = float(input('tax: ')) / 100
    calc = input('ggr ou ngr: ')
    print(calculate_share_rate(value, tax, calc))
