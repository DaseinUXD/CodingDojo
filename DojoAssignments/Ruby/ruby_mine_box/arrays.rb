array = ['one', 'two', 'three']
arrayNew = %w[`four` `five` `six`]



# .at or .fetch
puts array.at(0)
puts array.fetch(2)

# .delete
# array.delete('one')
# puts array
# .reverse
puts array.reverse

# .length
puts array.length

# .sort
puts array.sort

# .slice
puts array.slice(1, 2)

# .shuffle
puts array.shuffle


# .join
puts array.join('::')

# .insert
array.insert(3, 'four')
puts array
# values_at() -> returns an array with values specified in the param
puts arrayNew
puts arrayNew.values_at(1, 2).join(':-:')

