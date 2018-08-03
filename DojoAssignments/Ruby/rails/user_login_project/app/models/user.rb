class User < ApplicationRecord
  # EMAIL_REGEX = /\A[\w+\-.]+@[a-z\d\-]+(\.[a-z\d\-]+)*\.[a-z]+\z/i
  validates :first_name, :last_name, presence: true, length: { in: 2..20 }
  validates :age, numericality: true
  validates_numericality_of :age, greater_than: 10, less_than: 150
  # validates :email_address, presence: true, uniqueness: {case_sensitive: false}, format: {with: EMAIL_REGEX}
end
