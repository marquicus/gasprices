"""
		This will generate datapackage.json file
"""
import datapackage

package = datapackage.Package()
package.descriptor['name'] = 'Gas Prices'
package.descriptor['title'] = 'Gas Prices by Day and Month'

package.infer('gas_by*.csv')

print("Packaging data")
package.save('datapackage.json')
print("Done")

# End of file
# vim: set ts=2 sw=2 noet:

