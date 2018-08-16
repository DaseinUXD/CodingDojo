class Blog < ApplicationRecord
  has_many :users, through: :owners
  has_many :users, through: :posts
  has_many :comments, as: :usable
end
