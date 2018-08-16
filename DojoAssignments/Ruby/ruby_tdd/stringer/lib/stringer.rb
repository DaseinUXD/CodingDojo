require "stringer/version"

module Stringer
  # Your code goes here...
  def self.spacify (*strings)
    string = ""
    strings.each do |s|
      string += " " + s
      string = string.lstrip
    end
    string
  end

  def self.minify(string, max)
    if string.length > max
      string.slice(0..max) + '...'
    else
      string.slice(0..max)
    end

  end

  def self.replacify(in_string, replace, with)
    in_string.sub(replace, with)
  end

  def self.tokenize(string)
    string.split
  end

  def self.removify(string, to_remove)
    # string.delete!(to_remove)
    s = string
    r = to_remove
    r << " "
    s.slice! r
    s
  end

end
