class CreateResults < ActiveRecord::Migration[5.2]
  def change
    create_table :results do |t|
      t.string :name
      t.string :location
      t.string :language
      t.text :comments

      t.timestamps
    end
  end
end
