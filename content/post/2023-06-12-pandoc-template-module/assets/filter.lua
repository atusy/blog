--[[ assets/filter.lua ]]

---テキストファイルを読む
---@param filepath string テンプレートのファイルパス。相対パスの基準はPandoc実行時の作業ディレクトリ。
---@return string テンプレートの中身
local function read_lines(filepath)
  local lines = {}
  for i in io.lines(filepath) do
    table.insert(lines, i)
  end
  return table.concat(lines, "\n")
end

---テンプレートファイルを指定したコンテキスト化で展開し、Markdownとして処理する
---@param filepath string テンプレートのファイルパス。相対パスの基準はPandoc実行時の作業ディレクトリ。
---@param context table<any, any>
---@return any blocks PandocのBlock要素のリスト
local function apply_template(filepath, context)
  local content = read_lines(filepath)
  local compiled = pandoc.template.compile(content)
  local rendered = pandoc.template.apply(compiled, context):render()
  return pandoc.read(rendered, "markdown", PANDOC_READER_OPTIONS).blocks
end

---divのtemplate属性にファイルが指定されていれば、divの属性をコンテキストとしてテンプレートを展開するフィルタ
function Div(el)
  if el.attributes.template then
    local ctx = {}
    for k, v in pairs(el.attributes) do
      ctx[k] = v
    end
    return apply_template(el.attributes.template, ctx)
  end
  return el
end
