README - Verificador de Carteira e Chaves XRP

Descrição:

Este projeto fornece ferramentas para verificar carteiras XRP e chaves públicas e privadas. Ele permite que você:

    Verifica se uma carteira XRP é válida.
    Verifique se uma chave pública XRP é válida.
    Verifique se uma chave privada XRP é válida.
    Obtenha o endereço XRP de carteira.
    Obtenha o endereço XRP de uma chave pública.
    Obtenha a chave pública de uma chave privada.

Instalação:

git clone https://github.com/shadowruge/xrp_validate.git

Uso:
python gen_wallet_xrp.py #gera a carteira em .json
contendo :

     "addresses":"8bcFNcaLXJXCmoDEVaYwVkqE9ox6HeFc"
     "private_keys":"252075be323a2a8b05b7d453666357822feddd40b373cb802f1235acb457a018"
     "public_keys":"z5556e4063ba1b5b73adc0df5b56b850bc8f494d3d02ea190db1fafd276931b1fa20156572f7eb5f0830f332e63818e95ab730f6c6fd53b748eb060e52711e97"
    
  
Exemplo de uso:

python xrp_validator.py 

Saída:

A carteira rN938923892389238923892389238923 é válida.

Documentação:

Para mais informações, consulte a documentação completa em https://xrpl.org/run-rippled-as-a-validator.html.

Licença:

Este projeto é licenciado sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.

Contribuições:

São bem-vindas contribuições para este projeto. Consulte o arquivo CONTRIBUTING.md para mais informações.

Agradecimentos:

Agradecemos a todos que contribuíram para este projeto.
