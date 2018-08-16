class Comment < ApplicationRecord
  belongs_to :usable, polymorphic: true
end
