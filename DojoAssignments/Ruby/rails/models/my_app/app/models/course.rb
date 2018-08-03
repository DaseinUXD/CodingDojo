class Course < ApplicationRecord
  has_many :signups
  has_many :students, through: :signups
end
