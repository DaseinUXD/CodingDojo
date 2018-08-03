class User < ApplicationRecord
  EMAIL_REGEX = /\A[\w+\-.]+@[a-z\d\-]+(\.[a-z\d\-]+)*\.[a-z]+\z/i
  has_many :owners
  has_many :messages
  has_many :posts
  validates :first_name, :last_name, :email_address, presence: true
  validates :first_name, :last_name, length: { minimum: 2 }
  validates :email_address, uniqueness: { case_sensitive: false }, format: {with: EMAIL_REGEX}

end
