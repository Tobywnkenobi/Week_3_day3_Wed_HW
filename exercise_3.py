"""
### Exercise #3 <br>
<p>Convert the list below from Celsius to Farhenheit, using the map function with a lambda...</p>

`Output: [('Nashua', 89.6), ('Boston', 53.6), ('Los Angelos', 111.2), ('Miami', 84.2)]
`



# F = (9/5)*C + 32
places = [('Nashua',32),("Boston",12),("Los Angelos",44),("Miami",29)]
"""
# F = (9/5)*C + 32

places = [('Nashua',32),("Boston",12),("Los Angelos",44),("Miami",29)]

conv_to_fahr = list(map(lambda city: (city[0], (9/5)*city[1] + 32), places))

print(conv_to_fahr)
