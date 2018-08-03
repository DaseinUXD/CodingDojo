class User < ApplicationRecord
  EMAIL_REGEX = /\A[\w+\-.]+@[a-z\d\-]+(\.[a-z\d\-]+)*\.[a-z]+\z/i
  validates :first_name, :last_name, presence: true, length: { in: 2..20 }
  validates :email, presence: true, uniqueness: { case_sensitive: false }, format: { with: EMAIL_REGEX }

  # creating a custom instance method, self refers to the AplicationRecord object
  def full_name
    "#{first_name} #{last_name}"
  end

  # creating a custom class method. self refers to the User model
  def self.average_age
    sum(:age) / count
  end

  # this callback will run before saving on create and update
  before_save :downcase_email

  # this callback will run after creating a new user
  after_create :successfully_created

  # this callback will run after updating an existing user
  after_update :successfully_updated

  # this callback will only  run on creating a record to ensure a default age of 0
  before_validation :default_age, on: [:create]

  private

  def downcase_email
    email.downcase
  end

  def successfully_created
    puts 'Successfully created a new user'
  end

  def successfully_updated
    puts 'Successfully updated an existing user'
  end

  def default_age
    self.age = 0 unless self.age?
  end
end
