vim.g.mapleader = " "
vim.g.maplocalleader = " "

local opt = vim.opt
opt.number = true
opt.relativenumber = true
opt.mouse = "a"
opt.clipboard = "unnamedplus"
opt.tabstop = 2
opt.shiftwidth = 2
opt.expandtab = true
opt.smartindent = true
opt.wrap = false
opt.ignorecase = true
opt.smartcase = true
opt.cursorline = true
opt.termguicolors = true
opt.signcolumn = "yes"
opt.splitright = true
opt.splitbelow = true
opt.scrolloff = 8
opt.updatetime = 250
opt.laststatus = 3
opt.showmode = false
opt.spell = true
opt.spelllang = { "en_us" }
opt.spelloptions = "camel"

vim.diagnostic.config({
  virtual_text = {
    prefix = "●",
    spacing = 4,
  },
  underline = true,
  update_in_insert = true,
  severity_sort = true,
  float = {
    border = "rounded",
    source = true,
  },
  signs = {
    text = {
      [vim.diagnostic.severity.ERROR] = "✘",
      [vim.diagnostic.severity.WARN] = "▲",
      [vim.diagnostic.severity.HINT] = "⚑",
      [vim.diagnostic.severity.INFO] = "»",
    },
  },
})

vim.api.nvim_create_autocmd("ColorScheme", {
  callback = function()
    vim.api.nvim_set_hl(0, "SpellBad", { undercurl = true, sp = "#f44747" })
    vim.api.nvim_set_hl(0, "SpellCap", { undercurl = true, sp = "#cca700" })
    vim.api.nvim_set_hl(0, "SpellRare", { undercurl = true, sp = "#c586c0" })
    vim.api.nvim_set_hl(0, "SpellLocal", { undercurl = true, sp = "#4ec9b0" })
  end,
})

local keymap = vim.keymap.set
keymap("n", "<Esc>", "<cmd>nohlsearch<CR>")
keymap("n", "<C-s>", "<cmd>w<CR>")
keymap("n", "<C-h>", "<C-w>h")
keymap("n", "<C-j>", "<C-w>j")
keymap("n", "<C-k>", "<C-w>k")
keymap("n", "<C-l>", "<C-w>l")
keymap("n", "<leader>sv", "<C-w>v")
keymap("n", "<leader>sh", "<C-w>s")
keymap("n", "<leader>sx", "<cmd>close<CR>")
keymap("n", "<S-l>", "<cmd>bnext<CR>")
keymap("n", "<S-h>", "<cmd>bprevious<CR>")
keymap("n", "<leader>bd", "<cmd>bdelete<CR>")
keymap("n", "<leader>d", vim.diagnostic.open_float)
keymap("n", "[d", function()
  vim.diagnostic.jump({ count = -1, float = true })
end)
keymap("n", "]d", function()
  vim.diagnostic.jump({ count = 1, float = true })
end)

local lazypath = vim.fn.stdpath("data") .. "/lazy/lazy.nvim"
if not (vim.uv or vim.loop).fs_stat(lazypath) then
  vim.fn.system({
    "git",
    "clone",
    "--filter=blob:none",
    "https://github.com/folke/lazy.nvim.git",
    "--branch=stable",
    lazypath,
  })
end
vim.opt.rtp:prepend(lazypath)

require("lazy").setup("plugins", {
  change_detection = { notify = false },
})
