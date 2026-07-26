#!/bin/bash

# ==========================================
# Ragnar OS - Atualizador Git
# Autor: Dom + ChatGPT
# ==========================================

GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}"
echo "========================================="
echo "        RAGNAR GIT UPDATER"
echo "========================================="
echo -e "${NC}"

# Verifica se está em um repositório Git
if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
    echo -e "${RED}Erro: esta pasta não é um repositório Git.${NC}"
    exit 1
fi

echo -e "${YELLOW}Atualizando repositório...${NC}"
git pull

echo
echo -e "${YELLOW}Status:${NC}"
git status

echo
read -p "Mensagem do commit (Enter = automática): " MSG

if [ -z "$MSG" ]; then
    MSG="Atualização $(date '+%d/%m/%Y %H:%M')"
fi

git add .

if git diff --cached --quiet; then
    echo
    echo -e "${GREEN}Nenhuma alteração para enviar.${NC}"
    exit 0
fi

echo
echo -e "${YELLOW}Criando commit...${NC}"
git commit -m "$MSG"

echo
echo -e "${YELLOW}Enviando para o GitHub...${NC}"
git push

echo
echo -e "${GREEN}"
echo "========================================="
echo "      ✓ Atualização concluída!"
echo "========================================="
echo -e "${NC}"

