class Dojo < ApplicationRecord
  has_many :students, :dependent => :delete_all
  validates :branch, :street, :city, :state, presence: true
  validates :state, length: { is: 2 }
end
