class User < ApplicationRecord
  has_many :blogs, through: :owners
  has_many :blogs, through: :posts
  has_many :comments, as: :usable
end
