CodeBlock = function(el)
  local classes = el.attr.classes
  if classes == nil or #classes == 0 then return end
  return {
    pandoc.RawBlock("html", [[<details open><summary>]] .. classes[1] .. [[</summary>]]),
    el,
    pandoc.RawBlock("html", [[</summary>]])
  }
end
