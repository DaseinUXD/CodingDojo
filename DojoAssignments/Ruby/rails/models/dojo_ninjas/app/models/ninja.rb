class Ninja < ApplicationRecord
  belongs_to :dojo
  validates :first_name, :last_name, presence: true

  # has_one :dojo
end
