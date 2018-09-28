require_relative './tester/tester'
require_relative './tester/csv_exporter'
require_relative './sorts/insertion'
require_relative './sorts/heap'
require_relative './sorts/merge'
require_relative './sorts/quick'


class RubyDefault
  def sort(array)
    array.sort
  end
end

tester = Tester.new(max_len: 14)
csv_exporter = CSVExporter.new

insertion, sizes = tester.execute_all(Insertion.new, Heap.new, Merge.new, RubyDefault.new)

csv_exporter.export_map("test.csv", sizes, insertion)