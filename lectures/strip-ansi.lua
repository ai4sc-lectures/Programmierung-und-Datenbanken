-- Jupyter error tracebacks contain ANSI color escapes. Typst prints them as
-- garbage, so remove them for typst output (HTML renders them as colors).
if FORMAT:match("typst") then
  function CodeBlock(el)
    local text = el.text:gsub("\27%[[%d;]*m", "")
    if text ~= el.text then
      el.text = text
      return el
    end
  end
end
