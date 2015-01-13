products = [
		{'description':'guinness','price':'16.90'},
		{'description':'corona','price':'15.90'},
		{'description':'paulaner','price':'17.68'},
		{'description':'jupiter','price':'13.99'},
		{'description':'duvel','price':'18.90'},
		{'description':'chimay','price':'26.90'},
		{'description':'floris_fraise','price':'21.50'},
		{'description':'honey_dew','price':'32.80'},
		{'description':'cacilds','price':'19.99'},
		{'description':'weihenstephaner','price':'16.56'},
		{'description':'faxe_red','price':'12.90'}
]

cheap = heapq.nsmallest(1, products, key=lambda s: s['price'])
expensive = heapq.nlargest(1, products, key=lambda s: s['price'])
