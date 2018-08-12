# SSH and global IP options check
# Input:
#        global dictionary with defined dictionaries inside it: global_params = {'ip':{'ssh': {}, 'active service': {}}
#        config result dictionary
# Output:
#        updated result dictionary
#

def check(global_params):
    results_dict = {'IP options':{'SSH':{},'service':{}}}
# ssh section
    if 'version' in global_params['ip']['ssh']:
        if global_params['ip']['ssh']['version'] == '2':
            results_dict['IP options']['SSH']['version'] = [2, '2']
        else:
            results_dict['IP options']['SSH']['version'] = [0, '1', 'Turn on SSH 2 mode only to secure you connection']
    else:
        results_dict    ['IP options']['SSH']['version'] = [1, 'Both', 'Not SSH version 2 mode only, you may want to turn '
                                                                       'this mode on']

    if 'authentication_retries' in global_params['ip']['ssh']:
        if int(global_params['ip']['ssh']['authentication_retries']) > 5:
            results_dict['IP options']['SSH']['authentication retries'] = [1, str(global_params['ip']['ssh']['authentication_retries']),
                                                                           'You may want to decrease it']
        else:
            results_dict['IP options']['SSH']['authentication retries'] = [2, str(global_params['ip']['ssh']['authentication_retries'])]

    if 'time-out' in global_params['ip']['ssh']:
        if         int(global_params['ip']['ssh']['time-out']) < 100:
            results_dict['IP options']['SSH']['time-out'] = [2, str(global_params['ip']['ssh']['time-out'])]
        elif 100 < int(global_params['ip']['ssh']['time-out']) <= 300:
            results_dict['IP options']['SSH']['time-out'] = [1, str(global_params['ip']['ssh']['time-out']),
                                                     'You may want to decrease it']
        elif       int(global_params['ip']['ssh']['time-out']) > 300:
            results_dict['IP options']['SSH']['time-out'] = [0, str(global_params['ip']['ssh']['time-out']),
                                                             'Decrease it due to security reasons']

    if 'maxstartups' in global_params['ip']['ssh']:
        if int(global_params['ip']['ssh']['maxstartups']) < 5:
            results_dict['IP options']['SSH']['max startups'] = [2, str(global_params['ip']['ssh']['maxstartups'])]
        else:
            results_dict['IP options']['SSH']['max startups'] = [1, str(global_params['ip']['ssh']['maxstartups']),
                                                             'You may want to decrease it']

# ip options section
    if 'finger' in global_params['ip']['active_service']:
        results_dict['IP options']['service']['finger'] = [0, 'ENABLED',
                                                           'Disable it to prevent user to view other active users']
    else:
        results_dict['IP options']['service']['finger'] = [2, 'DISABLED']

    if 'identd' in global_params['ip']['active_service']:
        results_dict['IP options']['service']['identd'] = [0, 'ENABLED',
                                                           'Disable it to prevent user connection information leaks']
    else:
        results_dict['IP options']['service']['identd'] = [2, 'DISABLED']

    if 'source-route' in global_params['ip']['active_service']:
        results_dict['IP options']['service']['source-route'] = [0, 'ENABLED',
                                                                 'Disable it to prevent packet route leak']
    else:
        results_dict['IP options']['service']['source-route'] = [2, 'DISABLED']

    if 'bootp server' in global_params['ip']['active_service']:
        results_dict['IP options']['service']['bootp server'] = [0, 'ENABLED',
                                                                 'Disable it to prevent possible IOS image stealing']
    else:
        results_dict['IP options']['service']['bootp server'] = [2, 'DISABLED']

    if 'http server' in global_params['ip']['active_service']:
        results_dict['IP options']['service']['HTTP server'] = [0, 'ENABLED',
                                                                'Disable it to prevent unsecure connection. You may turn '
                                                                'on secure server with "ip http secure-server" command']
    else:
        results_dict['IP options']['service']['HTTP server'] = [2, 'DISABLED']

    return results_dict
