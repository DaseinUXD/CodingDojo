class Post < ApplicationRecord
  belongs_to :blog
  belongs_to :user
  has_many :users, through: :owners
  has_many :messages, dependent: :destroy
  validates :title, :content, presence: true
  validates :content, length: { minimum: 7 }
end
