import threading

#Retorna o número de objetos Thread atualmente ativos.
#A contagem retornada é igual ao comprimento da lista retornada por enumerate().
#print(threading.active_count())

#Retorna o objeto Thread atual, correspondente ao thread de controle do chamador.
#Se o encadeamento de controle do chamador não foi criado por meio do módulo de encadeamento,
#um objeto de encadeamento fictício com funcionalidade limitada é retornado.
#print(threading.current_thread())

#Manipular exceção não capturada gerada por Thread.run().
#O argumento args tem os seguintes atributos:
#exc_type: tipo de exceção. 
#exc_value: Valor de exceção, pode ser Nenhum. 
#exc_traceback: Traceback de exceção, pode ser Nenhum. 
#thread: Thread que gerou a exceção, pode ser None.
#print(threading.excepthook(args, /))

#Retorna o 'identificador de thread' do thread atual.
#Este é um número inteiro diferente de zero. Seu valor não tem significado direto;
#destina-se como um cookie mágico para ser usado, por exemplo.
# para indexar um dicionário de dados específicos de thread.
#Os identificadores de thread podem ser reciclados quando um thread sai e outro thread é criado.
#print(threading.get_ident())

#Retorne o ID de Thread integral nativo do thread atual atribuído pelo kernel.
#  Este é um número inteiro não negativo.
#Seu valor pode ser usado para identificar exclusivamente esse encadeamento 
# específico em todo o sistema (até que o encadeamento termine, 
# após o que o valor pode ser reciclado pelo sistema operacional).
#print(threading.get_native_id())

#Retorna uma lista de todos os Threadobjetos atualmente ativos. 
# A lista inclui threads daemonic e objetos de thread fictícios criados por current_thread().
#  Exclui encadeamentos encerrados e encadeamentos que ainda não foram iniciados.
#  No entanto, o encadeamento principal sempre faz parte do resultado, mesmo quando finalizado.
#print(threading.enumerate())

#Retorne o Threadobjeto principal. Em condições normais, o encadeamento
# principal é o encadeamento a partir do qual o interpretador Python foi iniciado.
#print(threading.main_thread( ))

#Defina uma função de rastreamento para todos os encadeamentos iniciados a partir
#  do módulo de encadeamento. O func será passado para sys.settrace() para cada thread,
#  antes que seu método run() seja chamado.
#print(threading.settrace(func))

#Obtenha a função de rastreamento conforme definido por settrace().
#print(threading.gettrace( ))

#Defina uma função de perfil para todos os encadeamentos iniciados 
# a partir do threadingmódulo. A função será passada sys.setprofile()
# para cada thread, antes que seu run()método seja chamado.
#print(threading.setprofile(função))

#Obtenha a função do criador de perfil conforme definido por setprofile().
#threading.getprofile( ) 

#Retorna o tamanho da pilha de threads usado ao criar novos threads.
#  O argumento de tamanho opcional especifica o tamanho da pilha a 
# ser usado para encadeamentos criados posteriormente e deve ser 0 
# (usar plataforma ou padrão configurado) ou um valor inteiro positivo
#  de pelo menos 32.768 (32 KiB). Se o tamanho não for especificado,
#  0 será usado. Se a alteração do tamanho da pilha de encadeamentos 
# não for compatível, a RuntimeErrorserá gerado. Se o tamanho da pilha
#  especificado for inválido, umValueErroré aumentado e o tamanho da pilha
#  não é modificado. 32 KiB é atualmente o valor mínimo de tamanho de pilha
#  suportado para garantir espaço de pilha suficiente para o próprio interpretador.
#  Observe que algumas plataformas podem ter restrições particulares em valores para 
# o tamanho da pilha, como exigir um tamanho mínimo de pilha > 32 KiB ou exigir alocação
#  em múltiplos do tamanho da página de memória do sistema - a documentação 
# da plataforma deve ser consultada para mais informações (páginas de 4 KiB são comuns;
#  usar múltiplos de 4096 para o tamanho da pilha é a abordagem sugerida na ausência de
#  informações mais específicas).
#threading.stack_size( [ tamanho ] )

#O valor máximo permitido para o parâmetro timeout das funções de bloqueio 
# ( Lock.acquire(), RLock.acquire(), Condition.wait(), etc.). 
# Especificar um tempo limite maior que esse valor gerará um arquivo OverflowError.
#threading.TIMEOUT_MAX

# x = threading.Thread(target=thread_function, args=(1,))
# logging.info("Main    : before running thread")
# x.start()
#class threading.Thread(
#    group = None ,     # grupo deve ser None; reservado para extensão futura quando uma ThreadGroupclasse for implementada.
#    target = None ,    # target é o objeto chamável a ser invocado pelo run() método. O padrão é None, o que significa que nada é chamado.
#    name = None ,      # name é o nome do thread. Por padrão, um nome exclusivo é construído na forma “Thread- N ” onde N é um pequeno número decimal, ou “Thread- N (target)” onde “target” é target.__name__se o argumento de destino for especificado.
#    args = () ,        # args é a tupla de argumentos para a invocação de destino. Padrões para ().
#    kwargs = {} ,      # kwargs é um dicionário de argumentos de palavras-chave para a invocação de destino. Padrões para {}.
#    * ,                # Caso contrário None, o daemon define explicitamente se o encadeamento é daemônico. Se None(o padrão), a propriedade daemonic é herdada do thread atual.
#    daemon = None )    # Se a subclasse substituir o construtor, ela deve ter certeza de invocar o construtor da classe base ( Thread.__init__()) antes de fazer qualquer outra coisa no thread.

#start( )    # Inicie a atividade do thread. deve ser chamado um vez no objeto
#run( )      # Método que representa a atividade do thread.
#join(timeout=None) # Aguarde até que o thread termine
#name        # Uma string usada apenas para fins de identificação. Não tem semântica. Vários segmentos podem receber o mesmo nome. O nome inicial é definido pelo construtor.
#getName( )  #API getter/setter obsoleta para name; use-o diretamente como uma propriedade.
#setName( )
#ident       #Este é um número inteiro diferente de zero. 
#native_id   #Esse valor pode ser usado para identificar exclusivamente esse encadeamento 
#is_alive( ) #Retorna se o thread está ativo.
#isDaemon( ) #API getter/setter obsoleta para daemon; use-o diretamente como uma propriedade.
#setDaemon( ) 
#