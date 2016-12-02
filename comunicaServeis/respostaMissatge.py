class CallbackqueryCommand extends SystemCommand
{
    protected $name = 'callbackquery';
    protected $description = 'Reply to callback query';

    // data before _ in callback query data => actual command
    private $commands = [
        'help' => 'help',
        'reply' => 'contact',
    ];

    public function execute()
    {
        $update = $this->getUpdate();
        $callback_query = $update->getCallbackQuery();
        $user_id = $callback_query->getFrom()->getId();
        $data = $callback_query->getData();

        $command = explode('_', $data);
        $command = $command[0];

        if (isset($this->commands[$command]) && $this->getTelegram()->getCommandObject($this->commands[$command])) {
            return $this->getTelegram()->executeCommand($this->commands[$command], $update);
        } else {
            $data = [];
            $data['callback_query_id'] = $callback_query->getId();
            $data['text'] = 'Invalid request!';
            $data['show_alert'] = true;
        }

        return Request::answerCallbackQuery($data);
    }
}
