class User < ApplicationRecord
  EMAIL_REGEX = /\A[\w+\-.]+@[a-z\d\-]+(\.[a-z\d\-]+)*\.[a-z]+\z/i
  validates :first_name, :last_name, :presence => true
  validates :email, uniqueness: {case_sensitive: false}
  validates :email, format: EMAIL_REGEX
end
