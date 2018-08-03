class Student < ApplicationRecord
  has_many :signups
  has_many :courses, through: :signups
end
