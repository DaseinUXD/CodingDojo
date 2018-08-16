class CreateComments < ActiveRecord::Migration[5.2]
  def change
    create_table :comments do |t|
      t.references :usable, polymorphic: true

      t.timestamps
    end
  end
end
